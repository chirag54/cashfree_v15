odoo.define("website_file_upload.file_upload", function (require) {
    "use strict";

  $(document).on('click', '#show_preview', function(){
    let pdffile=document.getElementById("attachment_1").files[0];
    if(pdffile)
    {
      let pdffile_url=URL.createObjectURL(pdffile);
      $('#viewer').attr('src',pdffile_url);
      $('#display_preview').css('display','block')
      $('#show_preview').css('display','none')
      $('#close_preview').css('display','block')
    }
    else{
      alert("Please Upload File!!!")
    }
});

  $(document).on('click', '#close_preview', function()
  {
    $('#display_preview').css('display','none')
    $('#show_preview').css('display','block')
    $('#close_preview').css('display','none')
  });


   
});
