import { FC } from 'react'
import { CheckBox, Group, Label } from 'components/Form'

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

interface GenresProps {
  onChange: (data: Record<string, boolean>) => void
}

const Genres: FC<GenresProps> = ({ onChange }) => {
  return (
    <Group>
      <Label>Жанры:</Label>

      {mocks.map(({ slug, name }, index) => (
        <CheckBox
          label={name}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
            onChange({ [slug]: e.target.checked })
          }}
          key={index}
        />
      ))}
    </Group>
  )
}

export { Genres }
