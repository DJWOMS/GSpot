import { FC } from 'react'
import { CheckBox, Group, Label } from 'components/Form'

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

interface PlatformsProps {
  onChange: (data: Record<string, boolean>) => void
}

const Platforms: FC<PlatformsProps> = ({ onChange }) => {
  return (
    <Group>
      <Label>Платформа: </Label>

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

export { Platforms }
