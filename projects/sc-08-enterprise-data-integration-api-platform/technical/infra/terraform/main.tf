terraform {
  required_version = ">= 1.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "aws" {}

provider "azurerm" {
  features {}
}

variable "aws_bucket_name" {
  type = string
}

variable "azure_resource_group" {
  type = string
}

variable "azure_location" {
  type    = string
  default = "westeurope"
}

variable "azure_storage_account" {
  type = string
}

resource "aws_s3_bucket" "landing" {
  bucket = var.aws_bucket_name
}

resource "azurerm_resource_group" "data" {
  name     = var.azure_resource_group
  location = var.azure_location
}

resource "azurerm_storage_account" "data" {
  name                     = var.azure_storage_account
  resource_group_name      = azurerm_resource_group.data.name
  location                 = azurerm_resource_group.data.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
