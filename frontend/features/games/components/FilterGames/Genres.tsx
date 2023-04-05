import { useEffect, useState } from 'react'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { FormGenreType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'

interface FormGenreTypeState extends FormGenreType {
  selected: boolean
}

const Genres = () => {
  const [genres, setGenres] = useState<FormGenreTypeState[] | null>(null)
  const toggleGenre = (selectedSlug: string) =>
    setGenres((genres) =>
      genres !== null
        ? genres.map((genre) => ({
            ...genre,
            selected: genre.slug === selectedSlug ? !genre.selected : genre.selected,
          }))
        : genres
    )

  const { getFilter, setFilter } = useFilter((state) => ({ getFilter: state.getFilter, setFilter: state.setFilter }))

  // update genres if changed
  useEffect(() => {
    setFilter(
      'genres',
      genres?.filter(({ selected }) => selected).map(({ slug }) => slug)
    )
  }, [genres, setFilter])

  // get list of genres from api and set {selected: true} for selected (from url query params)
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormGenreType[]>({
        path: '/games/filters/genres',
      })

      if (response) {
        const selectedGenres = getFilter('genres')
        setGenres(
          response.map((genre) => ({
            ...genre,
            selected: selectedGenres.includes(genre.slug),
          }))
        )
      }
    }

    loadData()
  }, [getFilter])

  return (
    <Group>
      <Label>Жанры:</Label>

      {genres === null ? (
        <SkeletonListCheckBoxes count={7} />
      ) : (
        genres.map(({ slug, name, selected }, index) => (
          <CheckBox label={name} defaultChecked={selected} onChange={() => toggleGenre(slug)} key={index} />
        ))
      )}
    </Group>
  )
}

export { Genres }
