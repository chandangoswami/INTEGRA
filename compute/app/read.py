
def from_files(spark, data_dir, pattern, format ):

    df = spark.\
        read.\
        format(format).\
        load(f'{data_dir}/{pattern}')
    return df