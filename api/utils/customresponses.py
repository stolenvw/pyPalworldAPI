responses = {
    404: {
        "description": "Item NotFound",
        "content": {"application/json": {"example": {"detail": "Nothing Found"}}},
    },
    400: {
        "description": "Missing params",
        "content": {"application/json": {"example": {"detail": "Missing params"}}},
    },
}
