import { useEffect, useState } from 'react'
import { useFormContext, Controller } from 'react-hook-form'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import type { FilterGenreInterface } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'

const Genres = () => {
  const [genres, setGenres] = useState<FilterGenreInterface[] | null>(null)
  const { control, watch } = useFormContext()

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

  const selectedGenres = watch('genres')

  return (
    <Group>
      <Label>Жанры:</Label>

      {genres === null ? (
        <SkeletonListCheckBoxes count={7} />
      ) : (
        genres.map(({ id, name, subgenres }) => (
          <>
            <Controller
              key={`g${id}`}
              control={control}
              name="genres"
              render={({ field }) => <CheckBox {...field} label={name} defaultValue={id} />}
            />

            {selectedGenres.includes(id.toFixed()) && subgenres.length > 0 && (
              <div className="mb-5 ml-5">
                {subgenres.map(({ id, name }) => (
                  <Controller
                    key={`s${id}`}
                    control={control}
                    name="subgenres"
                    render={({ field }) => <CheckBox label={name} defaultValue={id} {...field} />}
                  />
                ))}
              </div>
            )}
          </>
        ))
      )}
    </Group>
  )
}

export { Genres }
