import type { UserDataInterface } from 'features/profile/types'
import { fetchServerSide } from 'lib/fetchServerSide'
import ProfileForm from './ProfileForm'

const Profile = async () => {
  const data = await fetchServerSide<UserDataInterface | undefined>({
    path: '/profile/settings',
  })

  return <ProfileForm data={data} />
}

export default Profile
