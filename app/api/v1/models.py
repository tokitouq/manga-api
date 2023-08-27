from pydantic import BaseModel

# Response model for "/popular/" endpoint
class PopularMangaModel(BaseModel):
	rank: int
	title: str
	slug: str
	cover: str
	rating: float
	chapters: float
	volumes: float

# Response model for "/top-10/" endpoint
class TopTenMangaModel(BaseModel):
	rank: int
	title: str
	slug: str
	cover: str
	chapter: float
	synopsis: str
	genres: list[str]

# Response model for "/most-viewed/" endpoint
class MostViewedMangaModel(BaseModel):
	rank: int
	title: str
	slug: str
	cover: str
	views: int
	chapters: float
	volumes: float
	genres: list[str]