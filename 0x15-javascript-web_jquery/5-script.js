$('div#add_item').click(function () {
  let item = $('<li></li>').text('Item');
  $('ul.my_list').append(item);
});
