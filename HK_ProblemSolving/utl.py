qur=''
for day in range(1,31):
    data='''
    select dim_tab.md_date dt,promoid,coalesce(campaign.dc_client_name,dim_tab.app),
    dim_tab.app,dim_tab.operator,dim_tab.country geo,dim_tab.jspl_share jspl_share,
    coalesce(acq_count,0),coalesce(parking_count,0),coalesce(acq_rev,0),coalesce(ren_count,0),coalesce(grace_count,0),
    coalesce(ren_rev,0),coalesce(attempts,0),NOW()
    from
(select md_date,app,operator,country,jspl_share from product_operator,mis_dim_date where
 lower(product_operator.app) in ('comedyclub_batelco_bh','100mb_batelco_bh','droid_batelco_bh','droid_qa','100mb_etu'))
  dim_tab
    left outer join
    (select date(ma_date) dt,ma_app_user,ma_opt_name,
    case when ma_tokencall='notoken' or ma_tokencall=' ' or ma_tokencall like 'z_%' then 0 when ma_tokencall like '%-%' 
    then SUBSTRING_INDEX( SUBSTRING_INDEX(ma_tokencall,'-',3) ,'-',-1)else
    SUBSTRING_INDEX(SUBSTRING_INDEX(ma_tokencall,'#',3) , '#',-1) end as promoid,
    sum(case when ma_req_type='ACTIVATION' and ma_amount <> 0 then 1 else 0 end) acq_count,
    sum(case when ma_req_type='ACTIVATION' and ma_amount = 0 then 1 else 0 end) parking_count,
    sum(case when ma_req_type='ACTIVATION' then ma_amount else 0 end) acq_rev,
    sum(case when ma_req_type='RENEWAL' and ma_amount <> 0 then 1 else 0 end) ren_count,
    sum(case when ma_req_type='RENEWAL' and ma_amount = 0 then 1 else 0 end) grace_count,
    sum(case when ma_req_type='RENEWAL' then ma_amount else 0 end) ren_rev,
    sum(case when ma_user_status='ACTIVE' then 1 else 0 end) active_users,
    count(distinct ma_tranx_id) attempts
    from mis_activation_renewal
    where 
     date(ma_date) ='2020-07-'''+str(day)+'''' and ma_app_user in 
     ('comedyclub_batelco_bh','100mb_batelco_bh','droid_batelco_bh','droid_qa','100mb_etu')
    group by date(ma_date),ma_app_user,ma_opt_name,
    case when ma_tokencall='notoken' or ma_tokencall=' ' or ma_tokencall like 'z_%' then 0 
    when ma_tokencall like '%-%' 
    then SUBSTRING_INDEX( SUBSTRING_INDEX(ma_tokencall,'-',3) ,'-',-1)else
    SUBSTRING_INDEX(SUBSTRING_INDEX(ma_tokencall,'#',3) , '#',-1) end ) acq
    on (acq.ma_app_user=dim_tab.app and acq.ma_opt_name=dim_tab.operator)
    left outer join
    mis_dim_campaign campaign
    on (acq.promoid=campaign.dc_promo_id)
    where date(dim_tab.md_date) ='2020-07-'''+str(day)+''''
    '''
    qur=qur+data+'\n'+"union"
print(qur)