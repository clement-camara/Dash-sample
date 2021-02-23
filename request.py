request = """
    SELECT year AS years, value AS values , countries.name AS countries, flows.name AS flows, products.name AS products
        FROM quantities 
            JOIN countries 
                ON quantities.country_id = countries.id 
            JOIN flows 
                ON quantities.flow_id = flows.id
            JOIN products 
                ON products.id = quantities.product_id
            WHERE flows.name = 'Imports (ktoe)'
                AND products.name = 'Renewables and waste'
                AND products.name <> 'Total'
                ;
"""