


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
        body {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Montserrat', sans-serif;
        }
        .form-container {
            width: 100vw;
            height: 100vh;
            background-color: #7b2cbf;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .upload-files-container {
            background-color: #f7fff7;
            width: 420px;
            padding: 30px 60px;
            border-radius: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            box-shadow: rgba(0, 0, 0, 0.24) 0px 10px 20px, rgba(0, 0, 0, 0.28) 0px 6px 6px;
        }
        .drag-file-area {
            border: 2px dashed #7b2cbf;
            border-radius: 40px;
            margin: 10px 0 15px;
            padding: 30px 50px;
            width: 350px;
            text-align: center;
        }
        .drag-file-area .upload-icon {
            font-size: 50px;
        }
        .drag-file-area h3 {
            font-size: 26px;
            margin: 15px 0;
        }
        .drag-file-area label {
            font-size: 19px;
        }
        .drag-file-area label .browse-files-text {
            color: #7b2cbf;
            font-weight: bolder;
            cursor: pointer;
        }
        .browse-files span {
            position: relative;
            top: -25px;
        }
        .default-file-input {
            opacity: 0;
        }
        .cannot-upload-message {
            background-color: #ffc6c4;
            font-size: 17px;
            display: flex;
            align-items: center;
            margin: 5px 0;
            padding: 5px 10px 5px 30px;
            border-radius: 5px;
            color: #BB0000;
            display: none;
        }
        @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
        }
        .cannot-upload-message span, .upload-button-icon {
            padding-right: 10px;
        }
        .cannot-upload-message span:last-child {
            padding-left: 20px;
            cursor: pointer;
        }
        .file-block {
            color: #f7fff7;
            background-color: #7b2cbf;
            transition: all 1s;
            width: 390px;
            position: relative;
            display: none;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            margin: 10px 0 15px;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
        }
        .file-info {
            display: flex;
            align-items: center;
            font-size: 15px;
        }
        .file-icon {
            margin-right: 10px;
        }
        .file-name, .file-size {
            padding: 0 3px;
        }
        .remove-file-icon {
            cursor: pointer;
        }
        .progress-bar {
            display: flex;
            position: absolute;
            bottom: 0;
            left: 4.5%;
            width: 0;
            height: 5px;
            border-radius: 25px;
            background-color: #4BB543;
        }
        .upload-button {
            font-family: 'Montserrat';
            background-color: #7b2cbf;
            color: #f7fff7;
            display: flex;
            align-items: center;
            font-size: 18px;
            border: none;
            border-radius: 20px;
            margin: 10px;
            padding: 7.5px 50px;
            cursor: pointer;
        }
    </style>
</head>
<body>


    <link href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined" rel="stylesheet">
    <form class="form-container" enctype='multipart/form-data' method="POST">
        <div class="upload-files-container">
            <div class="drag-file-area">
                <span class="material-icons-outlined upload-icon"> file_upload </span>
                <h3 class="dynamic-message"> Drag & drop any file here </h3>
                <label class="label"> or <span class="browse-files"> <input name="file" type="file" class="default-file-input"/> <span class="browse-files-text">browse file</span> <span>from device</span> </span> </label>
            </div>
            <span class="cannot-upload-message"> <span class="material-icons-outlined">error</span> Please select a file first <span class="material-icons-outlined cancel-alert-button">cancel</span> </span>
            <div class="file-block">
                <div class="file-info"> <span class="material-icons-outlined file-icon">description</span> <span class="file-name"> </span> | <span class="file-size">  </span> </div>
                <span class="material-icons remove-file-icon">delete</span>
                <div class="progress-bar"> </div>
            </div>
            <input class="upload-button" type="submit" value="Submit">
        </div>
        <div class="upload-files-container" style="margin-left:50px;">
        <h1>Info</h1>

        <?php
            $ok = FALSE;
            echo "<pre>";
            print_r($_FILES);
            echo "</pre>";
            if($_FILES["file"]["error"]==0){
       
                $smth = end(explode(".",$_FILES['file']['name']));

                if (!file_exists(__DIR__.'/'.$smth)) {
                    mkdir(__DIR__.'/'.$smth, 0777, true); 
                    move_uploaded_file($_FILES["file"]["tmp_name"],__DIR__.'/'.$smth.'/'.$_FILES["file"]["name"]);
                    $ok=TRUE;
                }
                elseif(!file_exists(__DIR__.'/'.$smth.'/'.$_FILES['file']['name'])){
                    move_uploaded_file($_FILES["file"]["tmp_name"],__DIR__.'/'.$smth.'/'.$_FILES["file"]["name"]);
                    $ok=TRUE;
                }
                
            }
        ?>

        </div>
        <div class="upload-files-container" style="margin-left:50px;">
            <h1>
                <?php
                    if($_FILES["file"]["error"]==0){

                        if($ok==FALSE){
                            echo "Bu file bor!";
                        }
                        else{
                            echo "Success!";
                        }
                    }

                    else{
                        echo "Error!";
                    }
                ?>

            </h1>
        </div>
    </form>

</body>
</html>
