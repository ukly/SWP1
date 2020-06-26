html = """
<html>
    <body>
        <form method="get" action="">
            <p>
                a:  <input type="number" name="a" value="%(a)d">
            </p>
            <p>
                b:  <input type="number" name="b" value="%(b)d">
            </p>
            <p>
                <input type="submit" value="Submit">
            </p>
        </form>
        <p>
            Sum: %(sum1)d</br>
            Product: %(product1)d</br>
        </p>
    </body>
</html>
"""
