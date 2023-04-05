import { useEffect, useState } from 'react'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { FormGenreType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'

const Genres = () => {
  const [genres, setGenres] = useState<FormGenreType[] | null>(null)

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormGenreType[]>({
        path: '/games/filters/genres',
      })

      if (response) {
        setGenres(response)
      }
    }

    loadData()
  }, [])

  const toggleFilter = useFilter((state) => state.toggleFilter)

  return (
    <Group>
      <Label>Жанры:</Label>

      {genres === null ? (
        <SkeletonListCheckBoxes count={7} />
      ) : (
        genres.map(({ slug, name }, index) => (
          <CheckBox
            label={name}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
              toggleFilter('genres', slug, e.target.checked)
            }}
            key={index}
          />
        ))
      )}
    </Group>
  )
}

export { Genres }
