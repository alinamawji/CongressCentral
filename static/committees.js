$( document ).ready(function() {
    var sortedBy = "btnSortName";
    var sortedDirection = "down"

    // Sort by committee name
    $('#btnSortName').click(function (){
        // If already sorting by this value switch the order of sorting
        if (sortedBy == $(this).attr('id')) {
            if (sortedDirection == "down") {
                sortedDirection = "up"
            }
            else {
                sortedDirection = "down"
            }
        }
        // If not sorting by this value change the color of the buttons
        else {
            $("#"+sortedBy).removeClass("btn-primary").addClass("btn-secondary")
            sortedBy = $(this).attr('id')
            $("#"+sortedBy).removeClass("btn-secondary").addClass("btn-primary")
            sortedDirection = "down"
        }
        // Sort alphabetically or down
        if (sortedDirection == "down") {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".card-title").text() > $(b).find(".card-title").text() ? 1 : -1;
            }).appendTo("#card-container");
        }
        // Sort counter alphabetically or up
        else {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".card-title").text() < $(b).find(".card-title").text() ? 1 : -1;
            }).appendTo("#card-container");
        }
    })

    // Sort by chair name
    $('#btnSortChair').click(function (){
        // If already sorting by this value switch the order of sorting
        if (sortedBy == $(this).attr('id')) {
            if (sortedDirection == "down") {
                sortedDirection = "up"
            }
            else {
                sortedDirection = "down"
            }
        }
        // If not sorting by this value change the color of the buttons
        else {
            $("#"+sortedBy).removeClass("btn-primary").addClass("btn-secondary")
            sortedBy = $(this).attr('id')
            $("#"+sortedBy).removeClass("btn-secondary").addClass("btn-primary")
            sortedDirection = "down"
        }
        // Sort alphabetically or down
        if (sortedDirection == "down") {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".committee-chair").text() > $(b).find(".committee-chair").text() ? 1 : -1;
            }).appendTo("#card-container");
        }
        // Sort counter alphabetically or up
        else {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".committee-chair").text() < $(b).find(".committee-chair").text() ? 1 : -1;
            }).appendTo("#card-container");
        }
    })

    // Sort by ranking members name
    $('#btnSortRanking').click(function (){
        // If already sorting by this value switch the order of sorting
        if (sortedBy == $(this).attr('id')) {
            if (sortedDirection == "down") {
                sortedDirection = "up"
            }
            else {
                sortedDirection = "down"
            }
        }
        // If not sorting by this value change the color of the buttons
        else {
            $("#"+sortedBy).removeClass("btn-primary").addClass("btn-secondary")
            sortedBy = $(this).attr('id')
            $("#"+sortedBy).removeClass("btn-secondary").addClass("btn-primary")
            sortedDirection = "down"
        }
        // Sort alphabetically or down
        if (sortedDirection == "down") {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".committee-ranking").text() > $(b).find(".committee-ranking").text() ? 1 : -1;
            }).appendTo("#card-container");
        }
        // Sort counter alphabetically or up
        else {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".committee-ranking").text() < $(b).find(".committee-ranking").text() ? 1 : -1;
            }).appendTo("#card-container");
        }
    })

    // Sort by amount of members
    $('#btnSortMembers').click(function (){
        // If already sorting by this value switch the order of sorting
        if (sortedBy == $(this).attr('id')) {
            if (sortedDirection == "down") {
                sortedDirection = "up"
            }
            else {
                sortedDirection = "down"
            }
        }
        // If not sorting by this value change the color of the buttons
        else {
            $("#"+sortedBy).removeClass("btn-primary").addClass("btn-secondary")
            sortedBy = $(this).attr('id')
            $("#"+sortedBy).removeClass("btn-secondary").addClass("btn-primary")
            sortedDirection = "down"
        }
        // Sort least to most or down
        if (sortedDirection == "down") {
            $('#card-container .card-row').sort(function(a,b) {
                return ($(a).find(".majority-mems").children().length + $(a).find(".minority-mems").children().length)
                 > ($(b).find(".majority-mems").children().length + $(b).find(".minority-mems").children().length) ? 1 : -1;
            }).appendTo("#card-container");
        }
        // Sort most to least or up
        else {
            $('#card-container .card-row').sort(function(a,b) {
                return ($(a).find(".majority-mems").children().length + $(a).find(".minority-mems").children().length)
                 < ($(b).find(".majority-mems").children().length + $(b).find(".minority-mems").children().length) ? 1 : -1;
            }).appendTo("#card-container");
        }
    })

    // Sort by amount of subcommittees
    $('#btnSortSubcom').click(function (){
        // If already sorting by this value switch the order of sorting
        if (sortedBy == $(this).attr('id')) {
            if (sortedDirection == "down") {
                sortedDirection = "up"
            }
            else {
                sortedDirection = "down"
            }
        }
        // If not sorting by this value change the color of the buttons
        else {
            $("#"+sortedBy).removeClass("btn-primary").addClass("btn-secondary")
            sortedBy = $(this).attr('id')
            $("#"+sortedBy).removeClass("btn-secondary").addClass("btn-primary")
            sortedDirection = "down"
        }
        // Sort least to most or down
        if (sortedDirection == "down") {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".subcommittees").children().length > $(b).find(".subcommittees").children().length ? 1 : -1;
            }).appendTo("#card-container");
        }
        // Sort most to least or up
        else {
            $('#card-container .card-row').sort(function(a,b) {
                return $(a).find(".subcommittees").children().length < $(b).find(".subcommittees").children().length ? 1 : -1;
            }).appendTo("#card-container");
        }
    })

    // Sort by date of latest hearing
    $('#btnSortHearing').click(function (){
        // If already sorting by this value switch the order of sorting
        if (sortedBy == $(this).attr('id')) {
            if (sortedDirection == "down") {
                sortedDirection = "up"
            }
            else {
                sortedDirection = "down"
            }
        }
        // If not sorting by this value change the color of the buttons
        else {
            $("#"+sortedBy).removeClass("btn-primary").addClass("btn-secondary")
            sortedBy = $(this).attr('id')
            $("#"+sortedBy).removeClass("btn-secondary").addClass("btn-primary")
            sortedDirection = "down"
        }
        // FIXME: Parse as a date object
        // Sort sooner to later or down
        if (sortedDirection == "down") {
            $('#card-container .card-row').sort(function(a,b) {
                return Date.parse($(a).find(".latest-hearing").text()) < Date.parse($(b).find(".latest-hearing").text()) ? 1 : -1;
            }).appendTo("#card-container");
        }
        // Sort later to sooner or up
        else {
            $('#card-container .card-row').sort(function(a,b) {
                return Date.parse($(a).find(".latest-hearing").text()) > Date.parse($(b).find(".latest-hearing").text()) ? 1 : -1;
            }).appendTo("#card-container");
        }
    })
})
