import { AddItemToTable, ViewTableItems } from 'components'
import type { NextPage } from 'next'
import Head from 'next/head'


const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>Restaurant Client App</title>
        <meta name="description" content="App to manage orders" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <AddItemToTable />

      <ViewTableItems />
    </div>
  )
}

export default Home
