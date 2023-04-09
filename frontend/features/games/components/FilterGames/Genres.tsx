import { useEffect, useState } from 'react'
import { useFormContext } from 'react-hook-form'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { fetchServerSide } from 'lib/fetchServerSide'

type GenreState = {
  slug: string
  name: string
}

const Genres = () => {
  const [genres, setGenres] = useState<GenreState[] | null>(null)
  const { register } = useFormContext()

  // get list of genres from api and set {selected: true} for selected (from url query params)
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<GenreState[]>({
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
        genres.map(({ slug, name }, index) => <CheckBox label={name} defaultValue={slug} key={index} {...register('genres')} />)
      )}
    </Group>
  )
}

export { Genres }
