-- Create the procedure
CREATE OR REPLACE PROCEDURE clone_schema_with_privileges(
  existing_schema_name VARCHAR,
  new_schema_name VARCHAR,
  other_user_name VARCHAR)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS OWNER
AS
$$
DECLARE
  clone_sql STRING;
  grant_sql STRING;
BEGIN
  -- Step 1: Clone the schema
  clone_sql := 'CREATE SCHEMA ' || new_schema_name || ' CLONE ' || existing_schema_name;
  EXECUTE IMMEDIATE clone_sql;
  
  -- Step 2: Grant privileges to the other user
  grant_sql := 'GRANT USAGE, CREATE, MODIFY ON SCHEMA ' || new_schema_name || ' TO ' || other_user_name;
  EXECUTE IMMEDIATE grant_sql;
  
  RETURN 'Schema ' || new_schema_name || ' cloned successfully and privileges granted to ' || other_user_name || '.';
EXCEPTION
  WHEN OTHERS THEN
    RETURN 'Error: ' || SQLERRM;
END;
$$;
