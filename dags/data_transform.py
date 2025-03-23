def transform_data(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(key='extracted_data', task_ids='extract_from_api')
    print(f"Transforming {len(data)} records...")
    # Add your transformation logic here
    # Example: transformed_data = [modify(user) for user in data]
    # ti.xcom_push(key='transformed_data', value=transformed_data)
    pass