<?php
require_once "db.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"]);
    $age = trim($_POST["age"]);

    if (!empty($name) && !empty($age) && is_numeric($age)) {
        $stmt = $pdo->prepare("INSERT INTO records (name, age, status) VALUES (:name, :age, 0)");

        $stmt->execute([
            ":name" => $name,
            ":age" => $age
        ]);
    }
}

header("Location: index.php");
exit;
?>