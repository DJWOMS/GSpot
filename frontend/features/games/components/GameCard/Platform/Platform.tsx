import { FC } from 'react'
import { IconBrandApple, IconBrandWindows, IconBrandXbox, IconPlaystationSquare } from '@tabler/icons-react'
import cn from 'classnames'
import { PlatformType } from 'features/games'
import s from './Platform.module.scss'

const Platform: FC<PlatformType> = ({ type }): JSX.Element => {
  return (
    <div className={cn(s.platform, s[type])}>
      {type === 'xbox' && <IconBrandXbox />}
      {type === 'win' && <IconBrandWindows />}
      {type === 'ps' && <IconPlaystationSquare />}
      {type === 'ap' && <IconBrandApple />}
    </div>
  )
}

export { Platform }
