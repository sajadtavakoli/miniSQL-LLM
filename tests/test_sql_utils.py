from minisql_llm.sql_utils import normalize_sql, exact_match

def test_normalize_sql():
    assert normalize_sql(" SELECT  * FROM users; ") == "select * from users"

def test_exact_match():
    assert exact_match("SELECT * FROM users;", "select * from users")
