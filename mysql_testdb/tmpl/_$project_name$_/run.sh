#!/bin/bash

export HSEP="================================"
export DBMS_CMD="mysql -u_$mysql_user$_ -p_$mysql_pass$_"

echo -n "" && \
    echo -n "schema.sql:" && cat schema.sql | $DBMS_CMD && echo "DONE" &&\
    echo -n "data.sql:" && cat data.sql | $DBMS_CMD && echo "DONE" &&\
    echo $HSEP && \
    echo "fetch.sql:" && cat fetch.sql | $DBMS_CMD && echo "DONE" &&\
    echo $HSEP && \
    echo -n "close.sql:" && cat close.sql | $DBMS_CMD && echo "DONE"
