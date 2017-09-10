$(document).ready(function(){
    $('#domains-table').DataTable({
                processing: true,
                pageLength: 25,
                responsive: true,
                serverSide: true,
                sAjaxDataProp:"",
                responsive: true,
                ajax: {
                    url: '/api/me/dashboards',
                    type: 'GET',
                    dataSrc:"data",
                    beforeSend: function (xhr) {
                         xhr.setRequestHeader('Authorization', "Basic " + btoa(token + ":" + password));
                    }
                },

    });
    $('#seq-table').DataTable();
});