# TestT

#### Тести.
- [revenue](https://github.com/Grenui92/ad_media/blob/main/ad_media/revenue/tests.py)
- [spend](https://github.com/Grenui92/ad_media/blob/main/ad_media/spend/tests.py)

#### Документація зроблена за допомогою [drf_spectecular](https://drf-spectacular.readthedocs.io/en/latest/)
- за адресою "__your_domain__/api/schema/" - download .yaml
- за адресою "__your_domain__/api/docs/" - SWAGGER

#### SQLscript
<details>
<summary>spend</summary>

    select ss.name as spend_name,
        ss.date as spend_date,
        Sum(rr.revenue) as total_revenue,
        Sum(ss.spend) as total_spend,
        Sum(ss.impressions) as total_impression,
        Sum(ss.clicks) as total_clicks,
        Sum(ss."conversion") as total_conversion
    from spend_spendstatistic as ss
    left join 
    revenue_revenuestatistic as rr on rr.spend_id = ss.id
    group by ss.name, ss.date
</details>

<details>
<summary>revenue</summary>

    select rr.name, 
        rr.date,
        Sum(revenue) as total_revenue,
        Sum(ss.spend) as total_spend,
        Sum(ss.clicks) as total_clicks,
        Sum(ss."conversion") as total_conversion,
        Sum(ss.impressions) as total_impression
    from revenue_revenuestatistic as rr
    left join
    spend_spendstatistic as ss on rr.spend_id = ss.id
    group by rr.name, rr.date

</details>