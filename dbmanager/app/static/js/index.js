$(document).ready(function(){
    $('#domains-table').DataTable({
                processing: true,
                pageLength: 25,
                responsive: true,
                serverSide: true,
                sAjaxDataProp:"",
                responsive: true,
                ajax: {
                    url: '/domains',
                    type: 'GET',
                    dataSrc:"data",
                },
                columns: [
                    { "data": "id" },
                    { "data": "accession_number" },
                    { "data": "genus" },
                    { "data": "domain_model" },
                    { "data": "domain_description" },
                    { "data": "independent_eval" },
                    { "data": "first" },
                    { "data": "last" }
                ]

    });
    var seqTable = $('#seq-table').DataTable({
                processing: true,
                pageLength: 25,
                responsive: true,
                serverSide: true,
                sAjaxDataProp:"",
                responsive: true,
                ajax: {
                    url: '/sequences',
                    type: 'GET',
                    dataSrc:"data",
                },
                columns: [
                    { "data": "id" },
                    { "data": "accession_number" },
                    { "data": "genus" },
                    { "data": "protein_desc" },
                    { "data": "sequence" ,render :function(data,type,row){
                           if(type == 'display'){
                            var content = '';
                            content = content +     ' 	<a class="btn btn-default view-btn" href="#" >							   ';
                            content = content +     ' 		<i class="fa fa-ellipsis-h" title="View"></i>						   ';
                            return content;
                           }
                           return data;
                       }
                    }
                ]

    });
    $('#seq-table tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );
    seqTable.columns().every( function () {
        var that = this;

        $( 'input', this.footer() ).on( 'keyup change', function () {
            if ( that.search() !== this.value ) {
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );
});