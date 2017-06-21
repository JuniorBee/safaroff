/**
 * Created by alihaydar on 6/19/17.
 */
function get_page(page_number) {
    event.preventDefault();
    $.ajax({
        url: "?page="+page_number,
        type: "GET",
        success: function (html) {
            var post_container = $('#posts');
            post_container.append(html);
        }
    });
}
