import requests
import json
import time

CONGRESS = '117'
headers_pro = {'X-API-Key': 'X0BcSc7q8L5uuSHKNCCBaPrfrRReYzFOoOfZ3NNc'}
headers_twitter = {'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAAJLVNwEAAAAAI%2B5YAshrlnqagkKckBEbuoyMuVE%3DgCBjOjsaWj0A1LnaAPugVppvNMIQ90mvdE8gQhPIEpAOo6FJhc'}

members_table = []
twitter_account_table = []
financial_information_table = []
industry_contributors_table = []
organization_contributors_table = []
sector_contributors_table = []
committees_table = []
subcommittees_table = []
hearings_table = []
legislation_table = []
actions_table = []
are_part_of_table = []
is_pushed_through_table = []
discuss_table = []

def populate_committees_subcommittees_hearings_table(committees_table, subcommittees_table, hearings_table, discuss_table):
    url = 'https://api.propublica.org/congress/v1/' + CONGRESS + '/senate/committees.json'

    response = requests.get(url, headers=headers_pro)

    if response.status_code != 200:
        print("ERROR: committee API call failed")
        return
    else:
        print("Committee API call successful")

    table_list = response.json()
        
    for i in table_list['results'][0]['committees']:
        current_com = {'id': i['id'], 'name':i['name'], 'website':i['url'], 'branch':'senate',
        'chair_id':i['chair_id'], 'ranking_id':i['ranking_member_id']}
        print("APPEND: " + current_com['name'])
        committees_table.append(current_com)


        for j in i['subcommittees']:
            current_subcom = {'name':j['name'], 'committee_id':i['id']}
            print("APPEND: " + current_subcom['name'])
            subcommittees_table.append(current_subcom)


        url = 'https://api.propublica.org/congress/v1/' + CONGRESS + '/senate/committees/' + i['id'] + '/hearings.json'
        
        response = requests.get(url, headers=headers_pro)
        
        if response.status_code != 200:
            print("ERROR: hearings API call failed")
            continue
        
        current_hearing_com = response.json()

        for j in current_hearing_com['results'][0]['hearings']:
            current_hearing = {'date':j['date'], 'committee_id':i['id'], 'time':j['time'],
            'location':j['location'], 'description':j['description']}
            print("APPEND: " + current_hearing['committee_id'] + ' ' + current_hearing['date'])
            hearings_table.append(current_hearing)


            if j['bill_ids'] == []:
                print("APPEND: No bills discussed on " + current_hearing['date'])

            for k in j['bill_ids']:
                current_discussion = {'hearing_date':j['date'], 'hearing_time':j['time'],
                'hearing_location':j['location'], 'bill_id':k}
                print("APPEND: " + current_discussion['bill_id'] + ' ' + current_discussion['hearing_date'])
                discuss_table.append(current_discussion)


def populate_members_table(members_table, are_part_of_table, committees_table):
    url = 'https://api.propublica.org/congress/v1/' + CONGRESS + '/senate/members.json'

    response = requests.get(url, headers=headers_pro)

    if response.status_code != 200:
        print("ERROR: member API call failed")
        return
    else:
        print("Member API call successful")

    table_list = response.json()

    for i in table_list['results'][0]['members']:
        current_mem = {'id':i['id'], 'fname':i['first_name'], 'lname':i['last_name'], 'mname':i['middle_name'],
        'namesuffix':i['suffix'], 'party':i['party'], 'state':i['state'], 'state_rank':i['state_rank'], 
        'phone':i['phone'], 'mailing_address':i['office'], 'url':i['url']}
        if i['title'] in ['Resident Commissioner', 'Delegate']:
            current_mem['votes_w_party'] = None
            current_mem['votes_against_party'] = None
        else:
            current_mem['votes_w_party'] = i['votes_with_party_pct']
            current_mem['votes_against_party'] = i['votes_against_party_pct']
        print("APPEND: " + current_mem['id'])
        members_table.append(current_mem)

        url = 'https://api.propublica.org/congress/v1/members/' + i['id'] + '.json'
            
        response = requests.get(url, headers=headers_pro)
        
        if response.status_code != 200:
            print("ERROR: member API call failed")
            continue
        
        current_mem_coms = response.json()

        for j in current_mem_coms['results'][0]['roles'][0]['committees']:
            current_com = {'committee_id':j['code'], 'member_id':i['id']}
            print("APPEND: " + current_com['committee_id'] + ' for ' + current_com['member_id'])
            are_part_of_table.append(current_com)

            if j['title'] == "Chair":
                for k in committees_table:
                    if j['code'] == k['id']:
                        k['chair_id'] = i['id']
                        break
            if j['title'] == "Ranking Member":
                for k in committees_table:
                    if j['code'] == k['id']:
                        k['ranking_id'] = i['id']
                        break

def populate_twitter_account_table(twitter_account_table):
    url = 'https://api.propublica.org/congress/v1/' + CONGRESS + '/senate/members.json'

    response_pro = requests.get(url, headers=headers_pro)

    if response_pro.status_code != 200:
        print("ERROR: member API call failed")
        return
    else:
        print("Member API call successful")

    table_list = response_pro.json()

    for i in table_list['results'][0]['members']:
        current_twitter_account = {'member_id':i['id'], 'twitter_handle':i['twitter_account'], 'number_following':None,
        'number_followers':None, 'number_tweets':None, 'timeline_html':None}

        if current_twitter_account['twitter_handle'] == None:
            print("ERROR: No twitter handle for " + current_twitter_account['member_id'])
            continue
        else:
            url = 'https://api.twitter.com/1.1/users/show.json?screen_name=' + current_twitter_account['twitter_handle']
            response_twitter = requests.get(url, headers=headers_twitter)

            if response_twitter.status_code != 200:
                print("ERROR: twitter account " + current_twitter_account['twitter_handle'] + " does not exist")
                continue

            response_twitter = response_twitter.json()

            current_twitter_account['number_following'] = response_twitter['friends_count']
            current_twitter_account['number_followers'] = response_twitter['followers_count']
            current_twitter_account['number_tweets'] = response_twitter['statuses_count']

            url = 'https://publish.twitter.com/oembed?url=https://twitter.com/' + current_twitter_account['twitter_handle']
            response_twitter = requests.get(url, headers=headers_twitter)
            response_twitter = response_twitter.json()
            current_twitter_account['timeline_html'] = response_twitter['html']

            print("APPEND: " + current_twitter_account['twitter_handle'])
            twitter_account_table.append(current_twitter_account)


def populate_financial_information_tables(financial_information_table, industry_contributors_table, organization_contributors_table, sector_contributors_table):
    url = 'https://api.propublica.org/congress/v1/' + CONGRESS + '/senate/members.json'

    response = requests.get(url, headers=headers_pro)

    if response.status_code != 200:
        print("ERROR: member API call failed")
        return
    else:
        print("Member API call successful")

    table_list = response.json()

    for i in table_list['results'][0]['members']:
        current_mem = {'member_id':i['id'], 'crp_id':i['crp_id']}
        
        if i['crp_id'] == None:
            continue
            print('ERROR: No CRP ID found')

        print("APPEND: " + current_mem['member_id'])
        financial_information_table.append(current_mem)

        current_mem = i['crp_id']

        # Industries
        parameters_open = {'method':'candIndustry', 'cid':current_mem,
        'apikey':'94ffae42c3f1d027967ecd1b76ad33bc', 'output':'json'}
        url = 'https://www.opensecrets.org/api/?'
        response_open = requests.get(url, params=parameters_open)

        try:
            response_open = response_open.json()
            
            for j in response_open['response']['industries']['industry']:
                current_industry_contribution = {'crp_id':current_mem, 'industry_name':j['@attributes']['industry_name'],
                'total':j['@attributes']['total']}
                industry_contributors_table.append(current_industry_contribution)
            print("APPEND: " + current_mem + ' industry information')
        except:
            print("ERROR: industry contributors not found for " + current_mem)

        # Contributors
        parameters_open = {'method':'candContrib', 'cid':current_mem,
        'apikey':'94ffae42c3f1d027967ecd1b76ad33bc', 'output':'json'}
        url = 'https://www.opensecrets.org/api/?'
        response_open = requests.get(url, params=parameters_open)

        try:
            response_open = response_open.json()
            
            for j in response_open['response']['contributors']['contributor']:
                current_org_contribution = {'crp_id':current_mem, 'org_name':j['@attributes']['org_name'],
                'total':j['@attributes']['total']}
                organization_contributors_table.append(current_org_contribution)
            print("APPEND: " + current_mem + ' contributors information')
        except:
            print("ERROR: candidate contributors not found for " + current_mem)


        # Sectors
        parameters_open = {'method':'candSector', 'cid':current_mem,
        'apikey':'94ffae42c3f1d027967ecd1b76ad33bc', 'output':'json'}
        url = 'https://www.opensecrets.org/api/?'
        response_open = requests.get(url, params=parameters_open)

        try:
            response_open = response_open.json()
            
            for j in response_open['response']['sectors']['sector']:
                current_sect_contribution = {'crp_id':current_mem, 'sector_name':j['@attributes']['sector_name'],
                'total':j['@attributes']['total']}
                sector_contributors_table.append(current_sect_contribution)
            print("APPEND: " + current_mem + ' sector information')
        except:
            print("ERROR: sectors contributors not found for " + current_mem)


def populate_legislation_and_actions_table(legislation_table, actions_table, is_pushed_through_table):
    for i in members_table:
        url = 'https://api.propublica.org/congress/v1/members/' + i['id'] + '/bills/introduced.json'

        response = requests.get(url, headers=headers_pro)

        if response.status_code != 200:
            print('ERROR: member ' + i['id'] + ' bill information not found')
            continue

        table_list = response.json()

        for j in table_list['results'][0]['bills'][:10]:

            # prevents bill repeats
            bill_present = False
            for k in legislation_table:
                if bill_present:
                    break
                if k['bill_id'] == j['bill_id']:
                    bill_present = True
            if bill_present:
                continue

            current_leg = {'bill_id':j['bill_id'], 'cosponsors':j['cosponsors'], 'summary':j['title'], 'type':j['bill_type'],
            'date_introduced':j['introduced_date'], 'sponsor_id':j['sponsor_id'], 'bill_number':j['number']}
            print("APPEND: " + i['id'] + ' bill ' + current_leg['bill_number'])
            legislation_table.append(current_leg)

            current_leg_slug = j['bill_id'][:-4]

            url = 'https://api.propublica.org/congress/v1/' + CONGRESS + '/bills/' + current_leg_slug + '.json'

            response = requests.get(url, headers=headers_pro)

            sub_table_list = response.json()

            if sub_table_list['status'] != 'OK':
                print('ERROR: bill ' + current_leg_slug + ' information not found')
                continue

            for k in sub_table_list['results'][0]['committee_codes']:
                current_leg_com = {'committee_id':k, 'bill_id':j['bill_id']}
                print("APPEND: " + current_leg_com['bill_id'] + ': ' + current_leg_com['committee_id'])
                is_pushed_through_table.append(current_leg_com)

            for k in sub_table_list['results'][0]['actions']:
                current_action = {'action_id':str(k['id']), 'bill_id':j['bill_id'],
                'date':k['datetime'], 'description':k['description']}
                print("APPEND: " + current_action['bill_id'] + ': action ' + current_action['action_id'])
                actions_table.append(current_action)


def main():
    startTime = time.time()

    try:
        print('\n\nBEGINING COMMITTEES CALL\n\n')
        populate_committees_subcommittees_hearings_table(committees_table, subcommittees_table, hearings_table, discuss_table)
        with open('subcommittees_table.json', 'w', encoding='utf-8') as f:
            json.dump(subcommittees_table, f, ensure_ascii=False, indent=4)
        with open('hearings_table.json', 'w', encoding='utf-8') as f:
            json.dump(hearings_table, f, ensure_ascii=False, indent=4)
        with open('discuss_table.json', 'w', encoding='utf-8') as f:
            json.dump(discuss_table, f, ensure_ascii=False, indent=4)
        print('\n\nENDING COMMITTEES CALL\n\n')
    except:
        print('\n\nFAILURE ON COMMITTEES CALL\n\n')

    try:
        print('\n\nBEGINING MEMBERS CALL\n\n')
        populate_members_table(members_table, are_part_of_table, committees_table)
        with open('members_table.json', 'w', encoding='utf-8') as f:
            json.dump(members_table, f, ensure_ascii=False, indent=4)
        with open('are_part_of_table.json', 'w', encoding='utf-8') as f:
            json.dump(are_part_of_table, f, ensure_ascii=False, indent=4)
        with open('committees_table.json', 'w', encoding='utf-8') as f:
            json.dump(committees_table, f, ensure_ascii=False, indent=4)
        print('\n\nENDING MEMBERS CALL\n\n')
    except:
        print('\n\nFAILURE ON MEMBERS CALL\n\n')

    try:
        print('\n\nBEGINING TWITTER CALL\n\n')
        populate_twitter_account_table(twitter_account_table)
        with open('twitter_account_table.json', 'w', encoding='utf-8') as f:
            json.dump(twitter_account_table, f, ensure_ascii=False, indent=4)
        print('\n\nENDING TWITTER CALL\n\n')
    except:
        print('\n\nFAILURE ON TWITTER CALL\n\n')

    try:
        print('\n\nBEGINING FINANCIAL CALL\n\n')
        populate_financial_information_tables(financial_information_table, industry_contributors_table, organization_contributors_table, sector_contributors_table)
        with open('financial_information_table.json', 'w', encoding='utf-8') as f:
            json.dump(financial_information_table, f, ensure_ascii=False, indent=4)
        with open('industry_contributors_table.json', 'w', encoding='utf-8') as f:
            json.dump(industry_contributors_table, f, ensure_ascii=False, indent=4)
        with open('organization_contributors_table.json', 'w', encoding='utf-8') as f:
            json.dump(organization_contributors_table, f, ensure_ascii=False, indent=4)
        with open('sector_contributors_table.json', 'w', encoding='utf-8') as f:
            json.dump(sector_contributors_table, f, ensure_ascii=False, indent=4)
        print('\n\nENDING FINANCIAL CALL\n\n')
    except:
        print('\n\nFAILURE ON FINANCIAL CALL\n\n')

    try:
        print('\n\nBEGINING LEGISLATION CALL\n\n')
        populate_legislation_and_actions_table(legislation_table, actions_table, is_pushed_through_table)
        with open('legislation_table.json', 'w', encoding='utf-8') as f:
            json.dump(legislation_table, f, ensure_ascii=False, indent=4)
        with open('actions_table.json', 'w', encoding='utf-8') as f:
            json.dump(actions_table, f, ensure_ascii=False, indent=4)
        with open('is_pushed_through_table.json', 'w', encoding='utf-8') as f:
            json.dump(is_pushed_through_table, f, ensure_ascii=False, indent=4)
        print('\n\nENDING LEGISLATION CALL\n\n')
    except:
        print('\n\nFAILURE ON LEGISLATION CALL\n\n')

    print('\n\nENDING API CALLS\n\n')
    
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))

if __name__ == "__main__":
    main()

