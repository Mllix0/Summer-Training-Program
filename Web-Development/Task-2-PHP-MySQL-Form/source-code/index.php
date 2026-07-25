<?php
require_once "db.php";

$stmt = $pdo->query("SELECT * FROM records ORDER BY id DESC");
$records = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Task 2 - PHP MySQL Form</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

  <main class="page-container">

    <section class="hero-section">
      <p class="small-title">Web Development Task 2</p>
      <h1>PHP, MySQL Form and Status Toggle</h1>
      <p>
        This webpage allows users to submit a name and age, store the data in a MySQL database,
        display all records in a table, and toggle each record status between 0 and 1.
      </p>
    </section>

    <section class="card">
      <h2>Add New Record</h2>

      <form class="record-form" action="add_record.php" method="POST">
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" id="name" name="name" placeholder="Enter name" required>
        </div>

        <div class="form-group">
          <label for="age">Age</label>
          <input type="number" id="age" name="age" placeholder="Enter age" min="1" max="120" required>
        </div>

        <button type="submit" class="submit-btn">Submit</button>
      </form>
    </section>

    <section class="card">
      <div class="table-header">
        <div>
          <h2>Submitted Records</h2>
          <p>All records stored in the MySQL database are displayed below.</p>
        </div>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Age</th>
              <th>Status</th>
              <th>Created At</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            <?php if (count($records) > 0): ?>
              <?php foreach ($records as $record): ?>
                <tr id="record-<?php echo $record['id']; ?>">
                  <td><?php echo htmlspecialchars($record['id']); ?></td>
                  <td><?php echo htmlspecialchars($record['name']); ?></td>
                  <td><?php echo htmlspecialchars($record['age']); ?></td>
                  <td>
                    <span class="status-badge status-<?php echo $record['status']; ?>" id="status-<?php echo $record['id']; ?>">
                      <?php echo htmlspecialchars($record['status']); ?>
                    </span>
                  </td>
                  <td><?php echo htmlspecialchars($record['created_at']); ?></td>
                  <td>
                    <button class="toggle-btn" data-id="<?php echo $record['id']; ?>">
                      Toggle
                    </button>
                  </td>
                </tr>
              <?php endforeach; ?>
            <?php else: ?>
              <tr>
                <td colspan="6" class="empty-message">
                  No records yet. Add your first record using the form above.
                </td>
              </tr>
            <?php endif; ?>
          </tbody>
        </table>
      </div>
    </section>

  </main>

  <script src="assets/js/script.js"></script>
</body>
</html>