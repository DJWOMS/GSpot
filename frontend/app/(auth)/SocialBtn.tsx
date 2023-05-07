import { FC } from 'react'
import { IconBrandFacebook, IconBrandGoogle, IconBrandTwitter } from '@tabler/icons-react'
import cn from 'classnames'
import s from './Form.module.css'

interface Props {
  type: 'facebook' | 'google' | 'twitter'
}

const SocialBtn: FC<Props> = ({ type }) => {
  const { cn: className, icon } = getBtnProps(type)

  return <button className={cn(s.signSocial, className)}>{icon}</button>
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
