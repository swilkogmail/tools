https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration

/*
Create a policy for s3 access to profix
Create a role with the policy attached:
arn:aws:iam::265321640290:role/snowflake_access_role

*/

use database sandbox;
use role accountadmin;

CREATE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::265321640290:role/snowflake_access_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://snowflakeuploads/sybex/');

desc integration s3_int;

/* 

edit the policy and add the following

record the STORAGE_AWS_IAM_USER_ARN:
  arn:aws:iam::640411995588:user/cgfa0000-s

and STORAGE_AWS_EXTERNAL_ID:

  CY96277_SFCRole=2_hNlL4P5HkqC3BQ2ClUAOMo3qdD0=

*/


create or replace file format sandbox.public.my_csv_format
    TYPE = CSV
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1;

create or replace stage sandbox.public.my_s3_stage
  STORAGE_INTEGRATION = s3_int
  URL = 's3://snowflakeuploads/sybex/'
  file_format = my_csv_format;

LIST @sandbox.public.my_s3_stage
