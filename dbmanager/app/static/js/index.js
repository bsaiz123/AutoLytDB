$(document).ready(function(){
    var domTable = $('#domains-table').DataTable({
//                processing: true,
                pageLength: 25,
                responsive: true,
//                serverSide: true,
//                sAjaxDataProp:"",
//                responsive: true,
                sDom:"lrtip",
//                bFilter: false,
//                ajax: {
//                    url: '/domains',
//                    type: 'GET',
//                    dataSrc:"data",
//                },
//                columns: [
//                    { "data": "id" },
//                    { "data": "accession_number" },
//                    { "data": "genus" },
//                    { "data": "domain_model" },
//                    { "data": "domain_description" },
//                    { "data": "independent_eval" },
//                    { "data": "first" },
//                    { "data": "last" }
//                ]

    });
//    $('#domains-table tfoot th').each( function () {
//        var title = $(this).text();
//        $(this).html( '<input type="text" class="input-sm" placeholder="Search " />' );
//    } );
//    domTable.columns().every( function () {
//        var that = this;
//
//        $( 'input', this.footer() ).on( 'keyup change', function () {
//            if ( that.search() !== this.value ) {
//                that
//                    .search( this.value )
//                    .draw();
//            }
//        } );
//    } );
    var seqTable = $('#seq-table').DataTable({
                processing: true,
                pageLength: 25,
                responsive: true,
                serverSide: true,
                sAjaxDataProp:"",
                select: {
                    style: 'single'
                },
                sDom: "B<'row'><'row'<'col-md-6'l>r>t<'row'<'col-md-4'i>>p",
                buttons: [
                    {
                        text: 'Sequence Details',
                        action: function ( e, dt, node, config ) {
                            if(dt.rows('.selected').data().length > 0){
                                var accession_number = dt.rows('.selected').data()[0].accession_number;
                                window.location.href = '/details/'+accession_number;
                            }

                        }
                    }
                ],
//                bFilter: false,
                ajax: {
                    url: '/sequences',
                    type: 'GET',
                    dataSrc:"data",
                },
                columns: [
//                    { "data": "id" },
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
    $('#seq-table thead th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" /><br/>'+title );
    } );
    seqTable.columns().every( function () {
        var that = this;

        $( 'input', this.header() ).on( 'keyup change', function () {
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