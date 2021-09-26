def generate_html(container_data):
    with open("index.html", "w") as html:
        html.write("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <title>Docker</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;700&display=swap" rel="stylesheet">
                <style>
                    *{
                            border: 0;
                            box-sizing: border-box;
                            margin: 0;
                            padding: 0;
                            font-family: 'Ubuntu', sans-serif;
                    }
                    app{
                        background: rgb(33,71,79);
                        background: linear-gradient(0deg, rgba(33,71,79,1) 0%, rgba(5,169,203,1) 100%);
                        width: 100%;
                        height: 100%;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        min-height: 100vh;
                    }
                    h1{
                        color: white;
                        margin-top: 10px;
                    }

                    h2{
                        color: white;
                        margin-top: 15px;
                    }

                    .box{
                         display: flex;
                         flex-direction: column;
                        align-items: center;
                        background-color: white;
                        margin: 15px;
                        padding: 15px 25px;
                        border-radius: 25px;
                        min-width: 220px;
                        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.4);
                    }
                    .title{
                        margin-top: 10px;
                        font-weight: 700;
                        font-size: 16px;
                    }
                    .box img{
                        width: 70px;
                    }
                    .container_list{
                        display: flex;
                        width: 90%;
                        flex-wrap: wrap;
                        justify-content: center;
                    }
                </style>
            </head>
            <body>
            <app>
            <h1>Docker List</h1>
            """)
        last_dir = ""
        for container in container_data:
            if last_dir != container[3]:
                if last_dir != "": html.write("</div>")
                html.write("""
                        <h2>Diretório - {}</h2>
                    <div class='container_list'>
                """.format(container[3]))
            html.write("""
                <div class="box">
                    <img src="https://www.docker.com/sites/default/files/d8/2019-07/Moby-logo.png" />
                    <p class='title'>Name</p>
                    <p>{}</p>
                    <p class='title'>Status</p>
                    <p>{}</p>
                    <p class='title'>Image</p>
                    <p>{}</p>
                </div>
            """.format(container[1], container[2], container[4]))
            last_dir = container[3]
        html.write("</app></body>")