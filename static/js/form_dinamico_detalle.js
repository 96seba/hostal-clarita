var cont = 0;

function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    cont+=1;
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (cont-1) + '-','-' + cont + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (cont-1) + '-','-' + cont + '-');
        $(this).attr('for', newFor);
    });
    total++;

    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}

