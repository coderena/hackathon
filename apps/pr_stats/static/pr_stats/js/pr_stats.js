// this whole stuff should be rewritten to several classes.

//var ajax_url = 'http://localhost:6080/pr_stats.json';
var ajax_url = 'http://api.jcnrd.us/pr_stats.json';

function hide_instruction(hide) {
    if (hide) {
        $('.instruction-container').hide();
        $('.chart-container').show();
        $('#delete-chart-name').val('');
        $('#delete-chart-form').show();

    } else {
        $('.instruction-container').show();
        $('.chart-container').hide();
    }
}
function draw_chart_title(expr) {

    $('#chart-name').html('<a href="#save-query-dialog" role="button" data-toggle="modal" id="save-query">Save for future use!<a/>');
    $('#delete-chart-form').hide();
    $('#save-query').on('click', function() {
        $('#query-expr').val(expr);
        $('#query-name').val('');
        $('#query-category').val('');
    });
}
function draw_chart(expr, name, url) {
    hide_instruction(true);
    if (name) {
        $('#chart-name').html('<a title="View GNATS query results" href="' + url + '" target="_blank">' + name + '</a>');
    } else {
        draw_chart_title(expr);
    }

    $('#chart-expr').val(expr);
    $('#charts').html('');
    $.getJSON('?expr=' + encodeURIComponent(expr), function(data) {
        var subtitle = 'Year ' + moment().year();
        var parent = '#charts';
        catchup_chart(data, subtitle, transform_date_weekly, parent);
        state_distribution_chart(data, subtitle, transform_level_state, parent);
    });

}

function setup_indicator() {
    $.ajaxSetup({
        beforeSend:function(){
            // show gif here, eg:
            $("#loading").show();
        },
        complete:function(){
            // hide gif here, eg:
            $("#loading").hide();
        }
    });
}

function setup_sidenav() {
    $('.query').click(function() {
        var $this = $(this);
        draw_chart($this.data('expr'), $this.data('name'), $this.data('url'));
    });

    $('.instruction').click(function() {
        hide_instruction(false);
    });
}

function setup_query_form() {
    $('.form-search .btn').click(function() {
        var $node = $('.form-search .search-query');
        var expr = $node.val();
        if (!$.trim(expr)) return;
        $node.val('');
        draw_chart(expr);
    });
    return false;
}

function setup_save_form() {

    $('#save-query-btn').click(function() {
        var name = $.trim($('#query-name').val());
        var $info = $('#query-info');
        if (!name) {
            $info.text('Please specify a name');
        }
        var category = $('#query-category').val();
        if (!category) {
            $info.text('Please select a category');
        }
        var expr = $('#query-expr').val();
        $.post(ajax_url, {name:name, category:category, expr:expr}, function(data) {
            location.reload();
        })
    });
    return false;
}

function setup_delete_form() {
    $('#delete-chart').click(function() {
        var chart_name = $('#chart-name').text();
        var name = $('#delete-chart-name').val();

        if(chart_name != name) {
            alert('Please input the same name as current chart - ' + chart_name);
            return false;
        }
        $.ajax({
            url: ajax_url,
            type: 'DELETE',
            data: {name: chart_name},
            success: function(result) {
                location.reload();
            }
        });
    })
}

$(function() {

    setup_indicator();
    setup_sidenav();
    setup_query_form();
    setup_save_form();
    setup_delete_form();
})