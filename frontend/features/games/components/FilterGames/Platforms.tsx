import { CheckBox, Group, Label } from 'components/Form'
import { useFilter } from 'features/games/store'

const mocks = [
  {
    slug: 'ps',
    name: 'Playstation',
  },
  {
    slug: 'xb',
    name: 'XBOX',
  },
  {
    slug: 'wn',
    name: 'Windows',
  },
  {
    slug: 'mo',
    name: 'Mac OS',
  },
]

const Platforms = () => {
  const toggleFilter = useFilter((state) => state.toggleFilter)

  return (
    <Group>
      <Label>Платформа: </Label>

      {mocks.map(({ slug, name }, index) => (
        <CheckBox
          label={name}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
            toggleFilter('platforms', slug, e.target.checked)
          }}
          key={index}
        />
      ))}
    </Group>
  )
}

export { Platforms }
