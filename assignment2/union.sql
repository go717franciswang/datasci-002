select count(*)
from (
    select distinct term
    from frequency
    where docid in ('10398_txt_earn', '925_txt_trade') and count=1) a;
