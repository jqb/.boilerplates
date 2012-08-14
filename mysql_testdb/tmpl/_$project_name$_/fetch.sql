use _$project_name$_;


\! echo "Query 1";
          select users.id, users.name, tags.name as "tag name"
            from users
       left join user_tags on user_tags.user_id = users.id
       left join tags on user_tags.tag_id = tags.id
           where user_tags.user_id IS NULL
;


\! echo $HSEP
\! echo "Query 2";
          select users.id, users.name, GROUP_CONCAT(tags.name SEPARATOR ', ') as tags
            from users
            join user_tags on user_tags.user_id = users.id
            join tags on user_tags.tag_id = tags.id
        group by (users.id)
;
