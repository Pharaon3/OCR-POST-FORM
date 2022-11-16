<html>
<head>
<title>Run my Python files</title>
<?PHP
echo shell_exec("python test.py 'abc'");
echo "success!";
?>
</head>
