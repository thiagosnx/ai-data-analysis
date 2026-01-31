import streamlit as st
import pandas as pd
import pandas_gbq as bq

from services.data_extract_service import DataExtractService 
from services.data_transformation_service import DataTransformationService 

extract_service = DataExtractService()

# gbq
query_gbq = """
    with agg as 
        (select distinct
            initcap(nome) nome, 
            upper(marca) marca, 
            string_agg(
                tamanho, ', ' order by tamanho
            ) as tamanhos,
            preco_atual, 
            preco_real
        from `eco-avenue-461519-f8.telegramdata.shops`
        where 1=1
        and preco_atual < preco_real
        and disponivel = 1
        group by 
            nome, 
            marca, 
            preco_atual, 
            preco_real
        order by preco_atual, nome asc
    )

    select 
        nome,
        marca,
        case
            when lower(tamanhos) = 'default title'
            then 'U'
            else tamanhos
        end as tamanhos,
        preco_atual,
        preco_real
    from agg; 

"""
raw = extract_service.extract_data_gbq(query_gbq, "eco-avenue-461519-f8")


# query_mysql = """
# 		select distinct
# 		p.matricula,
# 		p.nome ,
# 		p.email ,
# 		p.estado,
# 		m.nome_modelo, 
# 		m.preco,
# 		p.created_at 
# 		from portgen.portfolios p
# 		join pagamentos pg on pg.id = p.id_pgto
# 		join modelos m on m.id = p.id_modelo 
# 		where 1=1
# 		and pg.status = 'approved';
# 		"""

# raw = extract_service.extract_data_mysql(query_mysql)

st.write(raw)
