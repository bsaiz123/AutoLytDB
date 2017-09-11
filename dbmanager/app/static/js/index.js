$(document).ready(function(){
    var domTable = $('#domains-table').DataTable({
                processing: true,
                pageLength: 25,
                responsive: true,
                serverSide: true,
                sAjaxDataProp:"",
                responsive: true,
                sDom:"lrtip",
//                bFilter: false,
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
    $('#domains-table tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" class="input-sm" placeholder="Search " />' );
    } );
    domTable.columns().every( function () {
        var that = this;

        $( 'input', this.footer() ).on( 'keyup change', function () {
            if ( that.search() !== this.value ) {
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );
    var seqTable = $('#seq-table').DataTable({
                processing: true,
                pageLength: 25,
                responsive: true,
                serverSide: true,
                sAjaxDataProp:"",
                responsive: true,
                sDom:"lrtip",
//                bFilter: false,
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
                            content = content +     ' 	<a class="btn btn-default view-btn" href="#" data-toggle="modal" data-target="#exampleModalLong" data-seq='+data+' >';
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
        $(this).html( '<input type="text" placeholder="Search " />' );
    } );
    seqTable.columns().every( function () {
        var that = this;

        $( 'input', this.footer() ).on( 'keyup change', function () {
            if ( that.search() !== this.value ) {
                that.search( this.value )
                    .draw();
            }
        } );
    } );
      $(document).on('click','.view-btn',function(e){
            $('#seq').text($(this).data('seq'));
           return true;
      });

});