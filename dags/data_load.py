def load_data(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(key='extracted_data', task_ids='extract_from_api')
    print(f"Loading {len(data)} records into PostgreSQL...")
    # Add PostgreSQL loading logic here
    pass