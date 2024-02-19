class SafeZoneService:
    async def get_safezone_data(self, db, latitude: float, longitude: float,
                                disaster_type: str, size: int = 10):
        query = f"""
        SELECT *, ST_DISTANCE(ST_GEOGPOINT({longitude}, {latitude}), location) AS distance
        FROM {db.dataset_id}.safezone
        CROSS JOIN UNNEST(disaster_type) as disaster
        WHERE disaster = '{disaster_type}' AND ST_DISTANCE(ST_GEOGPOINT({longitude}, {latitude}), location) <= 3000
        ORDER BY distance
        LIMIT {size};
        """

        query_job = db.client.query(query)
        results = query_job.result()

        return results