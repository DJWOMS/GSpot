import { CheckBox, Group, Label } from 'components/Form'
import { useFilter } from 'features/games/store'

const mocks = [
  {
    slug: 'adventure',
    name: 'Adventure',
  },
  {
    slug: 'fight',
    name: 'Fight',
  },
  {
    slug: 'sport',
    name: 'Sport',
  },
  {
    slug: 'action',
    name: 'Action',
  },
  {
    slug: 'rpg',
    name: 'RPG',
  },
  {
    slug: 'platform',
    name: 'Platform',
  },
]

const Genres = () => {
  const toggleFilter = useFilter((state) => state.toggleFilter)

  return (
    <Group>
      <Label>Жанры:</Label>

      {mocks.map(({ slug, name }, index) => (
        <CheckBox
          label={name}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
            toggleFilter('genres', slug, e.target.checked)
          }}
          key={index}
        />
      ))}
    </Group>
  )
}

export { Genres }
