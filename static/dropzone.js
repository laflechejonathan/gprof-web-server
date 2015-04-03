$(function() {
    var dropZone = $("#drop-zone");
    var profilerOutput = $("textarea#profiler_output");

    dropZone.on("drop", function(e) {
        e.preventDefault();
        this.className = 'upload-drop-zone';

        reader = new FileReader();

        reader.onload = function(e) {
            profilerOutput.val(reader.result);
        }

        filename = e.originalEvent.dataTransfer.files[0];
        reader.readAsText(filename)
    });

    dropZone.on("dragover", function() {
        this.className = 'upload-drop-zone drop';
        return false;
    });

    dropZone.on("dragleave", function() {
        this.className = 'upload-drop-zone';
        return false;
    });

})
