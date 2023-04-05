import { useState, useEffect } from 'react'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { FormPlatformType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'

interface FormPlatformTypeState extends FormPlatformType {
  selected: boolean
}

const Platforms = () => {
  const [platforms, setPlatforms] = useState<FormPlatformTypeState[] | null>(null)
  const togglePlatform = (selectedSlug: string) =>
    setPlatforms((platforms) =>
      platforms !== null
        ? platforms.map((platform) => ({
            ...platform,
            selected: platform.slug === selectedSlug ? !platform.selected : platform.selected,
          }))
        : platforms
    )

  const getFilter = useFilter((state) => state.getFilter)
  const setFilter = useFilter((state) => state.setFilter)

  // update genres if changed
  useEffect(() => {
    setFilter(
      'platforms',
      platforms?.filter(({ selected }) => selected).map(({ slug }) => slug)
    )
  }, [platforms, setFilter])

  // get list of platforms from api and set {selected: true} for selected (from url query params)
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormPlatformType[]>({
        path: '/games/filters/platforms',
      })

      if (response) {
        const selectedPlatforms = getFilter('platforms')
        setPlatforms(
          response.map((platform) => ({
            ...platform,
            selected: selectedPlatforms.includes(platform.slug),
          }))
        )
      }
    }

    loadData()
  }, [getFilter])

  return (
    <Group>
      <Label>Платформа: </Label>

      {platforms === null ? (
        <SkeletonListCheckBoxes count={4} />
      ) : (
        platforms.map(({ slug, name, selected }, index) => (
          <CheckBox label={name} defaultChecked={selected} onChange={() => togglePlatform(slug)} key={index} />
        ))
      )}
    </Group>
  )
}

export { Platforms }
