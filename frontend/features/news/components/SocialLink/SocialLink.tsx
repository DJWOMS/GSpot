import { FC } from 'react'
import { IconBrandFacebook, IconBrandTwitter, IconBrandVk } from '@tabler/icons-react'
import cn from 'classnames'
import s from './SocialLink.module.css'

interface Props {
  type: 'facebook' | 'twitter' | 'vk'
}

const SocialLink: FC<Props> = ({ type }) => {
  const { cn: className, icon, text } = getBtnProps(type)

  return (
    <a className={cn(s.link, className)}>
      {icon}
      {text}
    </a>
  )
}

const getBtnProps = (color: Props['type']) => {
  switch (color) {
    case 'facebook':
      return {
        icon: <IconBrandFacebook />,
        cn: s.facebook,
        text: 'share',
      }
    case 'twitter':
      return {
        icon: <IconBrandTwitter />,
        cn: s.twitter,
        text: 'tweet',
      }
    case 'vk':
      return {
        icon: <IconBrandVk />,
        cn: s.vkontakte,
        text: 'share',
      }
  }
}

export default SocialLink
