import { useEffect, useState } from 'react'
import { useFormContext } from 'react-hook-form'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { FilterGenreInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'

const Genres = () => {
  const [genres, setGenres] = useState<FilterGenreInterface[] | null>(null)
  const { register } = useFormContext()

  // get list of genres from api and set {selected: true} for selected (from url query params)
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FilterGenreInterface[]>({
        path: '/games/filters/genres',
      })

      if (response) {
        setGenres(response)
      }
    }

    loadData()
  }, [])

  return (
    <Group>
      <Label>Жанры:</Label>

      {genres === null ? (
        <SkeletonListCheckBoxes count={7} />
      ) : (
        genres.map(({ id, name }, index) => <CheckBox label={name} defaultValue={id} key={index} {...register('genres')} />)
      )}
    </Group>
  )
}

export { Genres }
