import { IconBrandFacebook, IconBrandGoogle, IconBrandTwitter } from '@tabler/icons-react'
import s from './Form.module.scss'
import { FC } from 'react'
import cn from 'classnames'

interface Props {
  type: 'facebook' | 'google' | 'twitter'
}

const SocialBtn: FC<Props> = ({ type }) => {
  const props = getBtnProps(type)

  return <button className={cn(s.signSocial, props.cn)}>{props.icon}</button>
}

const getBtnProps = (color: Props['type']) => {
  switch (color) {
    case 'facebook':
      return {
        icon: <IconBrandFacebook />,
        cn: s.signSocialFB,
      }
    case 'google':
      return {
        icon: <IconBrandGoogle />,
        cn: s.signSocialGL,
      }
    case 'twitter':
      return {
        icon: <IconBrandTwitter />,
        cn: s.signSocialTW,
      }
  }
}

export default SocialBtn
