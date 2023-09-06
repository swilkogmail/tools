/*
In order to streamline our time consuming and convoluted, object level, cloning procedure we would like to have the capability to clone our prod schema at the Schema level.

We would like to incorporate using the python connector in to our existing workfow with a simple procedure call.  One suggested implementation could be below:
*/

-- as admin user
CREATE OR REPLACE PROCEDURE clone_schema_with_privileges(new_schema_name VARCHAR)
RETURNS STRING
LANGUAGE SQL
EXECUTE AS OWNER
AS
$$
DECLARE
  clone_sql STRING;
  grant_sql STRING;
BEGIN

  clone_sql := 'CREATE SCHEMA ' || new_schema_name || ' CLONE MYDATASPACE.A205384_DEP_EAW';
  EXECUTE IMMEDIATE clone_sql;
 
  grant_sql := 'GRANT USAGE, CREATE, MODIFY ON SCHEMA ' || new_schema_name || ' TO a205384_dep_eaw_preprod_mds_owner';
  EXECUTE IMMEDIATE grant_sql;
 
  RETURN 'Clone Schema ' || new_schema_name || ' Created.';
EXCEPTION
  WHEN OTHERS THEN
    RETURN 'Error: ' || SQLERRM;
END;
$$;

-- grant to our role
grant usage on procedure clone_schema_with_privileges to a205384_dep_eaw_preprod_mds_owner;