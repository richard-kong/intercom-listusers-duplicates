# Duplicates in List Users

When using Intercom's [list-user](https://doc.intercom.io/api/#list-users) api, duplicate users are returned as we page through the results. 
My theory is that this is due to the sorting on `created_at`. For my app, we initially did a csv import so a large number of users have the same `created_at`. Sorting by this field could yield different results each time. 
Each time we read a page, the results are ordered slightly differently thus influencing which users appear on each page. The end effect is that some users appear more than once and some are missing entirely.

## What the script does

This script iterates through the pages from the `start_page` to the `end_page`. Once all pages have been read, it will print out the `id` of duplicate users along with the page numbers they were found in.

## How to use
Set the `intercom_api_key` and `intercom_app_id`, modify the `start_page` and `end_page` and run the script.