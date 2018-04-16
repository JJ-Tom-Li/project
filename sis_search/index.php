<html>
    <head>
        <?php
        include_once("news_query.php");
        
        $con = mysqli_connect("localhost","root","root");
        mysqli_select_db($con,"sis");
        $data = mysqli_query($con,"select * from news_header limit 60");

        ?>
        <script language="javascript">
            function search_by_title() {
                alert("123");
            }

            function search_by_author(input) {

            }

            function search_by_source(input) {

            }

            function search_by_body(input) {

            }

        </script>
    </head>
    <body>
        <div class="input">
            <form method="get" action="search_result.php">
                請輸入查詢內容:<br>
                利用標題查詢:<input type="text" name="search_by_title_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用作者查詢:<input type="text" name="search_by_author_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用內文查詢:<input type="text" name="search_by_body_input">
                <input type="submit" value="查詢"/><br>
            </form>
            <form method="get" action="search_result.php">
                利用新聞來源查詢:<input type="text" name="search_by_source_input">
                <input type="submit" value="查詢"/><br>
            </form>
        </div>
        <div class="show_result_table">
            <?php
                show_result_table($con,$data);
            ?>
        </div>
    </body>
</html>